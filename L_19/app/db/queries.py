ALL_SURVEYS = """SELECT * FROM surveys ORDER BY id"""

GET_SURVEY = """
SELECT s.id, s.title, s.description, s.created_by, s.created_at, s.is_anonymous, u.user_name
FROM surveys as s
LEFT JOIN users as u on u.id = s.created_by
WHERE s.id = %s;
"""

GET_OPTIONS_FOR_SURVEY = """
SELECT id, description
FROM options
WHERE survey_id = %s;
"""

GET_VOTES_FOR_SURVEY = """
SELECT o.description, count(v_o.id) as vote_count
FROM votes as v
JOIN vote_options as v_o on v.id = v_o.vote_id
JOIN options as o on o.id = v_o.option_id
WHERE v.survey_id = %s
GROUP BY o.description;
"""

GET_USER_BY_USERNAME_AND_PASSWORD = """
SELECT id, user_name
FROM users
WHERE user_name = %s and password = %s;
"""

GET_USER_BY_USERNAME = """
SELECT id, user_name, password
FROM users
WHERE user_name = %s;
"""

CREATE_USER = """
INSERT INTO users (user_name, password)
VALUES (%s, %s)
RETURNING id, user_name;
"""

CREATE_SURVEY = """
INSERT INTO surveys (title, description, created_by, is_anonymous)
VALUES (%s, %s, %s, %s)
RETURNING id, title, description, created_by, is_anonymous;
"""

CREATE_OPTION = """
INSERT INTO options (survey_id, description)
VALUES (%s, %s)
RETURNING id, description;
"""

CREATE_VOTE = """
INSERT INTO votes (survey_id, user_id, voter_ip)
VALUES (%s, %s, %s)
RETURNING id, survey_id, user_id;
"""

CREATE_VOTE_OPTIONS = """
INSERT INTO vote_options (vote_id, option_id)
VALUES (%s, %s)
RETURNING id, vote_id, option_id;
"""

CHECK_USER_VOTED = """
SELECT 1
FROM votes
WHERE survey_id = %s AND user_id = %s;
"""

CHECK_ANONYMOUS_USER_VOTED = """
SELECT 1
FROM votes
WHERE survey_id = %s AND voter_ip = %s;
"""

DELETE_SURVEY = """
DELETE FROM surveys
WHERE id = %s
RETURNING id;
"""