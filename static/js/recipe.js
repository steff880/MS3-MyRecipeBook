// Credit:
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
            <a href="#" class="remove-field text-shadow">Delete <i class="fas fa-trash-alt"></i></a>`;

        ingredientRow.append(newIngredientField);

    }
}

// Delete New Ingredient

$(ingredientRow).on('click', '.remove-field', function(e) {
    e.preventDefault();
    $(this).parent('div').remove();
    ingredient--;
});

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
            <a href="#" class="remove-step text-shadow">Delete <i class="fas fa-trash-alt"></i></a>`;
        // append to parent element
        methodRow.append(newStepField);
    }
}

// Delete step in method

$(methodRow).on('click', '.remove-step', function(e) {
    e.preventDefault();
    $(this).parent('div').remove();
    step--;
});

// Event Listeners

addStep.addEventListener('click', addNewStep)

addIngredient.addEventListener('click', appendIngredient);