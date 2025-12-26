use crate::{frame::Frame, graph::Node};
use anyhow::Result;
use opencv::imgcodecs;

pub struct SaveImage {
    pub path: String,
}

impl Node for SaveImage {
    fn process(&self, input: Frame) -> Result<Frame> {
        imgcodecs::imwrite(&self.path, &input.mat, &opencv::types::VectorOfi32::new())?;
        Ok(input)
    }
}
