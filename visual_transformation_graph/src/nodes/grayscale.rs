use crate::{frame::Frame, graph::Node};
use anyhow::Result;
use opencv::{imgproc, prelude::*};

pub struct Grayscale;

impl Node for Grayscale {
    fn process(&self, input: Frame) -> Result<Frame> {
        let mut gray = Mat::default();
        imgproc::cvt_color(&input.mat, &mut gray, imgproc::COLOR_BGR2GRAY, 0)?;
        Ok(Frame::new(gray))
    }
}
