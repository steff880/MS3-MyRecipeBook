<h1 align="center">MyRecipeBook</h1>

![Responsive](assets/img-readme/responsive.png)

## UX 
### Project Goals
The primary goal of **MyRecipeBook**, is to allow the users to _create_, _save_, _search_ and _view_ their favourite recipes in one place.

Use _HTML5_, _CSS3_, _JavaScript_, _Python_, _Flask_, and _MongoDB_
#### User Goals
The user is looking for web-based app where they can:
- Use CRUD convensions to:
    - Create a recipe
    - Read recipe
    - Update(Edit) recipe
    - Delete recipe they created
- Be able to search the database for recipes
### User Stories
**_As a first time visitor, I want to be:_**
- Able to easily find recipes stored in the database.
- Able to view full recipe and get valuable information.
- Able to Create and Account.

**_As a returning visitor, I want to be:_**
- Able to log into my account and have access to all features of the site.
- Able to Add(Create) recipes and store them in the database.
- Able to View my own recipes
- Able to Edit recipe
- Able to Delete a recipe(s) I have created.

**_As an Admin user of the site, I want to:_**
- Be able to add new categories

_Please note that currently Admin user can only add **categories**_

### Strategy

- For this project, the targeted audiences are:
    - Food Lovers
    - People, who are passionate about cooking
    - People of all ages
    
- The website enables the user to:
    - Register or Log in to account
    - View Recipes
    - Search Recipes, by category or name, even by ingredients
    - Create their own recipes and upload them to the database
    - View the full recipe they have created, or someone elses
    - Edit recipes they  have created
    - Delete a recipe created by them

### Scope

- What the user will look for:
    - Easy navigation
    - Welcoming Design
    - Search the database for recipes
    - Add their own recipe
    - Manage recipes (Edit, Delete)
    - Save and View full recipe
    - Be able to Register and Login

### Design

#### Colors

- Colors used for text:
    - #515251
    - #6A7359
    - #fff
- Background colors:
    - rgba(241, 183, 183, 0.29)
    - rgba(255, 255, 255, 0.28);
    - rgba(255, 255, 255, 0.8)
    - rgba(243, 222, 222, 0.3)
    - rgba(255, 255, 255, 0.4)
    - #f7e3e3
    - #f48b89
    - #6A7359
    - #515251
    - #eab0b1
    - #f5e9e9
    - #e06666
    - #ec7f7d

#### Typography

- The primary font used is **Poppins**, and **Sans Serif** is used as a fallback font.

#### Images
## Data Schema
[MongoDB](https://www.mongodb.com/) was used for this project and schema design was created. See below:

![Schema Design](assets/img-readme/updated-schema-design.png)

### Users Collection
- Upon regisering, the user will provide:
    - Username
    - Email Address
    - Password
    - is_admin is given a default value of False.

### Recipes Collection
- When creating a new recipe the user will provide the following:
    - Recipe Name
    - Recipe Image URL
    - Original Recipe URL(not required but needed to avoid copyright issues)
    - Category
    - Ingredients
    - Method
    - Prep Time (Total time needed to prepare the recipe)
    - Number of Serves
    - Created By (it will get a value of the current user in session)

### Categories Collection
- Currently there are four categories the user can choose from:
    - Main
    - Starter
    - Salad
    - Soup

### Subscribers Collection
- If the user decides to subscribe for the newsletter he/she will have to provide:
    - Email Addres (which is stored in the collection)
### Wireframes
[Wireframes part 1](https://github.com/steff880/MS3-MyRecipeBook/blob/main/assets/wireframes/wireframes-part1.png)

[Wireframes part 2](https://github.com/steff880/MS3-MyRecipeBook/blob/main/assets/wireframes/wireframes-part2.png)
## Features

- Each page has a responsive and fixed to the top navigation, in order for the user to be able at any moment to navigate to a different page.
- A class *active* is given to the current page link in the navigation, highlighting it for the user.

![Navigation](assets/img-readme/show-navigation.png)

![SideNavigation](assets/img-readme/side-navigation.png)

- The **_Footer_** of the site contains social media links and and Newsletter subscription

![Footer](assets/img-readme/footer.png)

- If the user is logged in their account, will have access to:
    - Profile page
    - Add Recipe page
    - Update Recipe
    - Delete Recipe
    - View Full Recipe
    - If the user is _admin_, then will have access to Manage Categories, where new categories can be added.
- The website uses _cards_ to display recipes, giving short info for the user:
    - Recipe image
    - Recipe Category
    - Recipe Name
    - Created by
    - A button to view full recipe

![RecipeCards](assets/img-readme/recipe-cards.png)

## Technologies Used
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
### Frameworks, Libraries & Programs Used
- [Materialize](https://materializecss.com/)
    - Materialize was used to help with the responsiveness and styling of the website. 
- [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used for creating the wireframes for this project.
- [jQuery](https://jquery.com/)
    - jQuery was mainly used to initialize some Materialize components.
- [Google Fonts](https://fonts.google.com/)
    - Google Fonts was used to import the **Poppins** font, which was used throughout the project.
- [Font Awesome](https://fontawesome.com/)
    - Font Awesome was used for all icons used in this project.
- [GitHub](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
- [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
## Resources
## Testing
## Deployment
## Credits
### Code
### Images
### Acknowledgements