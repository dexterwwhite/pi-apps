#[derive(Debug)]
pub struct Password {
    pub id: u32,
    pub site: String,
    pub username: String,
    pub password: String,
    pub email: String,
    pub notes: String,
    pub created: String, //datetime, auto
    pub last_modified: String
}