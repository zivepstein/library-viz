# library-viz
![alt text](https://github.com/zivepstein/library-viz/blob/master/app/screenshot.png)

This reposity serves as a wrapper for an academic digital library of PDFs. It uses a simple d3 + flask app to visualize and explore the library. It recursively builds a collection of nested circles representing the file structure of your library, where the size of the circles (which corresponds to actual papers) is their size. Using buttery d3 animation, you can zoom in and around your library with ease. 

Simply put the hierarchical file structure for your library in the main folder (i.e next to the `papers-we-love folder`). Then, simply run the below code

```
cd app
python app.py
```
then navigate to `http://127.0.0.1:5000/` to explore your files! 
