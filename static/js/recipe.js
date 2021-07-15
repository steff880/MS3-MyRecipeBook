// Code inspired from https://github.com/rebeccatraceyt/bake-it-til-you-make-it/blob/master/static/js/recipe.js
// Declare global variables

// Set max ingredients
let maxIngredients = 30;
let ingredientRow = document.getElementById('ingredient-row');
let addIngredient = document.getElementById('add-ingredient');
let ingredient = 1;

// Append new ingredient

const appendIngredient = (e) => {
    e.preventDefault();

    if (ingredient < maxIngredients) {
        ingredient++;
        let newIngredientField = document.createElement('div');
        newIngredientField.classList.add('input-field', 'col', 's12');
        newIngredientField.innerHTML = `
            <i class="fas fa-list-ul prefix form-icon"></i>
            <input type="text" id="ingredients" name="ingredients" minlength="3" class="validate" required>
            <span class="helper-text grey-text darken-3"> Enter new ingredient</span>
            <a id="delete-btn" href="#" class="remove-field text-shadow">Delete <i class="fas fa-trash-alt"></i></a>`;

        ingredientRow.append(newIngredientField);

    }
}

// Code inspired from https://stackoverflow.com/questions/30601620/adding-an-event-listener-to-an-element-that-doesnt-exist-yet-in-vanilla-javascr
// Delete New Ingredient

const deleteIngredient = (event) => {
    event.preventDefault();
    // Get clicked element
    let element = event.target;
    // check if clicked element has the class we need
    if (element.classList.contains('remove-field')) {
        // remove last ingredient
        if (ingredientRow.children.length > 1) {
            ingredientRow.lastChild.remove();
            ingredient--;
        }
    }
}

// Event Listeners

ingredientRow.addEventListener('click', deleteIngredient);

addIngredient.addEventListener('click', appendIngredient);