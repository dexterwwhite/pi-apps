use axum::{response::Json};
use serde_json::{Value, json};

pub async fn test() -> Json<Value> {
    Json(json!({ "Name":"Me", "Date":"10/25/2124" }))
}