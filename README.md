# Image Enhancer

This is a Flask web application that enhances the quality of uploaded images using the Replicate AI.

## Features

- Upload an image file.
- Compress the image file to improve performance.
- Use Replicate AI to enhance the image.
- Download and display the enhanced image.

## Prerequisites

- Python 3.x
- Flask
- Pillow
- Replicate
- urllib

## Installation

1. Clone the repository
2. Navigate to the directory
3. Install the dependencies
4. Run the application


The application will start running on `http://127.0.0.1:5000/`.

## Environment Variables

The application uses one environment variable:

- `REPLICATE_API_TOKEN`: Your Replicate API token. This should not be committed to the repository. Instead, set it in your environment before running the application.

For Heroku, you can set environment variables in the settings of your application dashboard.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
