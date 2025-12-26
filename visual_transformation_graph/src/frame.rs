use opencv::prelude::*;

#[derive(Clone)]
pub struct Frame {
    pub mat: Mat,
}

impl Frame {
    pub fn new(mat: Mat) -> Self {
        Self { mat }
    }
}
