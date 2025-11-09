from sqlalchemy import String, Text, DateTime, Boolean, ForeignKey, func, text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional
from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    tablename = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    # Relationships
    surveys: Mapped[list['Survey']] = relationship('Survey', back_populates='user')
    votes: Mapped[list['Vote']] = relationship('Vote', back_populates='user')


class Survey(Base):
    tablename = 'surveys'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_by: Mapped[Optional[int]] = mapped_column(
        ForeignKey('users.id', ondelete='SET NULL')
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    is_anonymous: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text('false')
    )

    # Relationships
    user: Mapped[Optional['User']] = relationship('User', back_populates='surveys')
    options: Mapped[list['Option']] = relationship('Option', back_populates='survey', cascade="all, delete")
    votes: Mapped[list['Vote']] = relationship('Vote', back_populates='survey', cascade="all, delete")


class Option(Base):
    tablename = 'options'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    survey_id: Mapped[int] = mapped_column(
        ForeignKey('surveys.id', ondelete='CASCADE'),
        nullable=False
    )

    # Relationships
    survey: Mapped['Survey'] = relationship('Survey', back_populates='options')
    vote_options: Mapped[list['VoteOption']] = relationship('VoteOption', back_populates='option',
                                                            cascade="all, delete")


class Vote(Base):
    tablename = 'votes'

    id: Mapped[int] = mapped_column(primary_key=True)
    survey_id: Mapped[int] = mapped_column(
        ForeignKey('surveys.id', ondelete='CASCADE'),
        nullable=False
    )
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('users.id', ondelete='SET NULL')
    )
    voter_ip: Mapped[Optional[str]] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    # Уникальные индексы как в вашей схеме
    table_args = (
        UniqueConstraint('survey_id', 'user_id', name='uq_survey_user'),
        UniqueConstraint('survey_id', 'voter_ip', name='uq_survey_voter_ip'),
    )

    # Relationships
    survey: Mapped['Survey'] = relationship('Survey', back_populates='votes')
    user: Mapped[Optional['User']] = relationship('User', back_populates='votes')
    vote_options: Mapped[list['VoteOption']] = relationship('VoteOption', back_populates='vote', cascade="all, delete")


class VoteOption(Base):
    tablename = 'vote_options'

    id: Mapped[int] = mapped_column(primary_key=True)
    vote_id: Mapped[int] = mapped_column(
        ForeignKey('votes.id', ondelete='CASCADE'),
        nullable=False
    )
    option_id: Mapped[int] = mapped_column(
        ForeignKey('options.id', ondelete='CASCADE'),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    # Уникальный индекс как в вашей схеме
    table_args = (
        UniqueConstraint('vote_id', 'option_id', name='uq_vote_option'),
    )

    # Relationships
    vote: Mapped['Vote'] = relationship('Vote', back_populates='vote_options')
    option: Mapped['Option'] = relationship('Option', back_populates='vote_options')