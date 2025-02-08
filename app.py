import gradio as gr
from src.model.vision_model import ChartVisionModel
import ollama

def analyze_chart(image):
    client = ollama.Client()
    
    system_prompt = """Analyze this technical chart and provide:
    1. Pattern Recognition (Support/Resistance, Trends)
    2. Technical Indicators Analysis
    3. Price Action Analysis
    4. Volume Analysis
    5. Future Price Predictions
    Format the response in clear sections."""
    
    response = client.generate(
        model="llama3.2-vision:latest",
        prompt=system_prompt,
        images=[image]
    )
    
    return response

interface = gr.Interface(
    fn=analyze_chart,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Analysis Results"),
    title="Technical Chart Analysis",
    description="Upload a chart image for comprehensive technical analysis"
)

interface.launch()
