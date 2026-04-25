pub mod auth;
pub mod test;

use axum::Router;

pub fn create_router() -> Router {
    Router::new()
        .nest("/test", test::routes())
}