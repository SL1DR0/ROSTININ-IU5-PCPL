use crate::{frame::Frame, graph::Node};
use anyhow::Result;
use opencv::{imgcodecs, prelude::*};

pub struct LoadImage {
    pub path: String,
}

impl Node for LoadImage {
    fn process(&self, _input: Frame) -> Result<Frame> {
        let mat = imgcodecs::imread(&self.path, imgcodecs::IMREAD_COLOR)?;
        Ok(Frame::new(mat))
    }
}
