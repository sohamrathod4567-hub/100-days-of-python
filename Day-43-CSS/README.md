# Day 43 – Introduction to CSS

## Overview

On Day 43 of the **100 Days of Code – The Complete Python Pro Bootcamp**, I started learning **CSS (Cascading Style Sheets)**.

The focus of today's lesson was understanding how CSS is used to style HTML elements and control the appearance of a webpage.

## Concepts Practiced

* Introduction to CSS
* CSS selectors
* Element selectors
* Class selectors
* ID selectors
* CSS properties and values
* Changing text colors
* Changing background colors
* Font size and styling
* Setting image height and width
* Using `px` and other CSS units
* Inline CSS
* Internal CSS
* External CSS
* Linking a CSS file to HTML

## How to Run

1. Clone or download this repository.
2. Navigate to the **Day-43** folder.
3. Open the HTML file in your browser.
4. Make sure the CSS file is correctly linked to the HTML file.

Example:

```html
<link rel="stylesheet" href="style.css">
```

## Example

### HTML

```html
<!DOCTYPE html>
<html>
<head>
    <title>Day 43 CSS</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1>Hello CSS!</h1>

    <p class="description">
        Learning CSS with 100 Days of Code.
    </p>

    <img src="image.jpg" class="profile-img">

</body>
</html>
```

### CSS

```css
h1 {
    color: blue;
}

.description {
    font-size: 20px;
}

.profile-img {
    width: 300px;
    height: 200px;
    object-fit: cover;
}
```

## What I Learned

Today I learned how **CSS works together with HTML** to control the design and appearance of webpages.

I learned how to select HTML elements and modify properties such as colors, sizes, backgrounds, fonts, and image dimensions.

I also learned the difference between **inline, internal, and external CSS**, with external CSS being useful for keeping the structure and styling of a website separate.

## Project Status

**Completed – Day 43 of 100 Days of Code**
