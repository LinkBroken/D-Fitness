
// Define exercisesList object containing exercise categories and their details

const exercisesList =
    {
"Abs": [ {
            name: "Hanging Leg Raises",
            image: "/static/images/abs/hanging leg raises.png"
        },
        {
            name: "Abdominal Crunches",
            image: "/static/images/abs/abdominal crunches.png"
        },
        {
            name: "Bicycle Crunch",
            image: "/static/images/abs/Bicycle Crunch.png"
        },
        {
            name: "Russian Twist",
            image: "/static/images/abs/Russian Twist.png"
        }
    ],
"Arms":[
    {
        name: "Tricep Kickbacks",
        image: "/static/images/arms/tricep kickbacks.png"
    },
    {
        name: "Overhead Tricep Extension",
        image: "/static/images/arms/overhead triceps extension.png"
    },
    {
        name: "Hammer Curls",
        image: "/static/images/arms/Hammer curls.png"
    },
    {
        name: "Bicep Curls",
        image: "/static/images/arms/bicep curls.png"
    }
],
"Legs":[  {
        name: "Squats",
        image: "/static/images/legs/squats.png"
    },
    {
        name: "leg Press",
        image: "/static/images/legs/leg press.png"
    },
    {
        name: "leg Extensions",
        image: "/static/images/legs/leg extension.png"
    },
    {
        name: "leg Curls",
        image: "/static/images/legs/leg curls.png"
    }
],
"Back":[  {
        name: "Lat Pulldowns",
        image: "/static/images/back/lat pulldowns.png"
    },
    {
        name: "Deadlifts",
        image: "/static/images/back/deadlift.png"
    },
    {
        name: "Single Hand dumbbell bent over row",
        image: "/static/images/back/single arm bent over row.png"
    },
    {
        name: "Barbell Bent Over Row",
        image: "/static/images/back/barbell bent over row.png"
    }
],
"Chest":[
    {
        name: "Barbell Bench Press",
        image: "/static/images/chest/barbell bench press.png"
    },
    {
        name: "Chest Flys",
        image: "/static/images/chest/dumbbell chest flys.png"
    },
    {
        name: "Dumbbell bench press",
        image: "/static/images/chest/dumbbell bench press.png"
    },
    {
        name: "Body weight Push Ups",
        image: "/static/images/chest/push ups.png"
    }
],
"Full body":[  {
        name: "Squats",
        image: "/static/images/fullbody/squats.png"
    },
    {
        name: "Bench press",
        image: "/static/images/fullbody/barbell bench press.png"
    },
    {
        name: "Pull Ups",
        image: "/static/images/fullbody/pullups.png"
    },
    {
        name: "Shoulder press",
        image: "/static/images/fullbody/shoulder press.png"
    }
]};

// Get HTML element with the class "exercises"
const divExercises = document.getElementsByClassName("exercises");

// Function to display exercises on the page
function displayContent(exercises) {
    // Loop through each exercise in the provided array
    for (let i = 0; i < exercises.length; i++) {
        // Create new elements for exercise details
        const newDiv = document.createElement("div");
        const h4 = document.createElement("h4");
        const image = document.createElement("img");
        const form = document.createElement("form")
        const sets = document.createElement("input");
        const reps = document.createElement("input");
        const addButton = document.createElement("input");
        const exerciseName = document.createElement("input")

        // Set classes and attributes for the new elements
        newDiv.classList = "exercise";
        sets.placeholder = "Sets";
        reps.placeholder = "Reps";
        h4.innerHTML = exercises[i]["name"];
        image.src = exercises[i]["image"];

        // Get current path from URL
        const path = window.location.href.split("/");
        const currentPath = path[path.length - 1]

        // Set form attributes
        form.method = "post";
        form.action = "/" + currentPath
        addButton.value = "Add";
        addButton.type = "submit";
        exerciseName.type = "text";
        exerciseName.value = h4.innerHTML;
        exerciseName.name = "exercise";
        exerciseName.readOnly = true

        // Set attributes for sets and reps inputs
        sets.type = "number";
        sets.name = "sets"
        sets.min = 1;
        sets.max = 4;

        reps.type = "number";
        reps.name = "reps"
        reps.min = 1;
        reps.max = 15;

        // Add event listener for form submission
        form.addEventListener("submit", function() {
            const formData = new FormData(form)

            // Send form data to server using fetch API
            fetch('/' + currentPath, {
                method: 'POST',
                body: formData
            }).then(response => {
                if (response.ok) {
                    window.prompt(('Added successfully.'));
                } else {
                    console.error('failed');
                }
            })
        })

        // Append elements to form
        form.append(sets, reps, exerciseName, addButton);

        // Append elements to newDiv
        newDiv.append(h4, image, form)

        // Append newDiv to divExercises element in the HTML
        divExercises[0].appendChild(newDiv)
    }
}

// Call displayContent function with exercises from the current category (document.title)
displayContent(exercisesList[document.title])