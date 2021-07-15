// Code inspired from https://github.com/rebeccatraceyt/bake-it-til-you-make-it/blob/master/static/js/recipe.js
// Declare global variables

// Set max ingredients
let maxIngredients = 30;
let ingredientRow = document.getElementById('ingredient-row');
let addIngredient = document.getElementById('add-ingredient');
let ingredient = 1;

// set max Method steps
let maxSteps = 30;
let methodRow = document.getElementById('method-row');
let addStep = document.getElementById('add-step');
let step = 1;

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

// Append new steps in Method

const addNewStep = (e) => {
    // prevent default action
    e.preventDefault();
    // check if step is less than max
    if (step < maxSteps) {
        step++;
        // create new div element
        let newStepField = document.createElement('div');
        // add classes to the element
        newStepField.classList.add('input-field', 'col', 's12');
        // set the inner HTML
        newStepField.innerHTML = `
            <i class="fas fa-list-ol prefix form-icon"></i>
            <textarea id="method" name="method" class="materialize-textarea validate" minlength="3"
                maxlength="300" rows="2" required></textarea>
            <span class="helper-text grey-text darken-3"> Enter new method step</span>
            <a id="delete-step-btn" href="#" class="remove-step text-shadow">Delete <i class="fas fa-trash-alt"></i></a>`;
        // append to parent element
        methodRow.append(newStepField);
    }
}

// Delete step in method

const deleteStep = (event) => {
    event.preventDefault();
    let element = event.target;

    if (element.classList.contains('remove-step')) {

        if (methodRow.children.length > 1) {
            methodRow.lastChild.remove();
            step--;
        }
    }
}

// Event Listeners
methodRow.addEventListener('click', deleteStep)

addStep.addEventListener('click', addNewStep)

ingredientRow.addEventListener('click', deleteIngredient);

addIngredient.addEventListener('click', appendIngredient);