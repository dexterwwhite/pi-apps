use axum::{Router, routing::get};

use crate::handlers::test;


pub fn routes() -> Router {
    Router::new()
        .route("/test-endpoint", get(test::test))
}