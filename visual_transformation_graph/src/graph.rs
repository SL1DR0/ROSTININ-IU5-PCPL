use crate::frame::Frame;
use anyhow::Result;

pub trait Node {
    fn process(&self, input: Frame) -> Result<Frame>;
}

pub struct Graph {
    nodes: Vec<Box<dyn Node>>,
}

impl Graph {
    pub fn new() -> Self {
        Self { nodes: Vec::new() }
    }

    pub fn add<N: Node + 'static>(mut self, node: N) -> Self {
        self.nodes.push(Box::new(node));
        self
    }

    pub fn run(&self, mut frame: Frame) -> Result<Frame> {
        for node in &self.nodes {
            frame = node.process(frame)?;
        }
        Ok(frame)
    }
}
