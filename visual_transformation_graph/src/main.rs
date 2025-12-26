mod frame;
mod graph;
mod nodes;

use anyhow::Result;
use frame::Frame;
use graph::Graph;
use nodes::{
    load::LoadImage,
    grayscale::Grayscale,
    save::SaveImage,
};

fn main() -> Result<()> {
    let empty = Frame::new(opencv::core::Mat::default());

    let graph = Graph::new()
        .add(LoadImage { path: "input.jpg".to_string() })
        .add(Grayscale)
        .add(SaveImage { path: "output.jpg".to_string() });

    graph.run(empty)?;

    println!("Pipeline executed successfully!");
    Ok(())
}
