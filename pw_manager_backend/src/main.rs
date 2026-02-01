use rusqlite::{params, Connection, Result};
mod models;
use crate::models::Password;

fn main() -> Result<()> {

    // Database setup
    let conn = Connection::open("name-from-env.db")?;
    conn.execute_batch(include_str!("migrations/001_init.sql"))?;

    let tp = Password {
        username: "jesser".to_string(),
        id: 3,
        notes: "".to_string(),
        site: "https://booglio-ooglibob.comst".to_string(),
        password: "ultimate-password!5555".to_string(),
        email: "jesser.libb@booglio-ooglibob.comst".to_string(),
        created: "Today".to_string(),
        last_modified: "Today".to_string()
    };

    let mut query = conn.prepare(
        "INSERT INTO password (id, site, username, password, email, notes, created, last_modified) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8)"
    )?;

    query.execute(params![tp.id, tp.site, tp.username, tp.password, tp.email, tp.notes, tp.created, tp.last_modified])?;

    let mut stmt = conn.prepare(
        "SELECT id, site, username, password, email, notes, created, last_modified FROM password"
    )?;

    let p_iter = stmt.query_map([], |row| {
        Ok(Password {
            id: row.get(0)?,
            site: row.get(1)?,
            username: row.get(2)?,
            password: row.get(3)?,
            email: row.get(4)?,
            notes: row.get(5)?,
            created: row.get(6)?,
            last_modified: row.get(7)?,
        })
    })?;

    for p in p_iter {
        println!("Found p {:?}", p?);
    }
    Ok(())

    // let mut stmt = conn.prepare(
    //     "INSERT INTO vault_items (user_id, ciphertext) VALUES (?1, ?2)"
    // )?;
    
    // stmt.execute(params![user_id, encrypted_blob])?;
    
}
