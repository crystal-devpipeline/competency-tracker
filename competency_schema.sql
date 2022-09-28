CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password_hash TEXT NOT NULL,
    date_created TEXT,
    hire_date TEXT,
    user_type TEXT,
    active INTEGER DEFAULT 1
);


CREATE TABLE IF NOT EXISTS Login_logout(
    login_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    active INTEGER DEFAULT 1
    FOREIGN KEY(user_id)
    REFERENCES User(user_id)
);

    0 = No competency - Needs Training and Direction    
    1 = Basic Competency - Needs Ongoing Support    
    2 = Intermediate Competency - Needs Occasional Support    
    3 = Advanced Competency - Completes Task Independently    
    4 = Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations

CREATE TABLE IF NOT EXISTS Competency(
    user_id INTEGER PRIMARY KEY,
    no_competency INTEGER,
    basic_competency INTEGER,
    intermediate_competency INTEGER,
    advanced_competency INTEGER,
    expert_competency INTEGER,
    FOREIGN KEY(user_id)
    REFERENCES User(user_id)
);

CREATE TABLE IF NOT EXISTS Assessments(
    needs_training INTEGER,
    needs_ongoing_support INTEGER,
    needs_occasional_support INTEGER,
    completes_task_independently INTEGER,
    effective_optimization INTEGER,
    FOREIGN KEY(user_id)
    REFERENCES User(user_id)
);

CREATE TABLE IF NOT EXISTS Assessment_results(
    user_id INTEGER,
    no_competency INTEGER,
    basic_competency INTEGER,
    intermediate_competency INTEGER,
    advanced_competency INTEGER,
    expert_competency INTEGER DEFAULT,
    FOREIGN KEY(user_id)
    REFERENCES User(user_id)
);
