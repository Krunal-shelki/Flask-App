let food = [
  {
    name: "Rice",
    unit: "100gm",
    calories: 130,
  },
  {
    name: "Moong Dal",
    unit: "100gm",
    calories: 115,
  },
   
  {
    name: "Atta Roti",
    unit: "1",
    calories: 71,
  },
  {
    name: "Pigeon Peas",
    unit: "100gm",
    calories: 343,
  },
 
  {
    name: "Chicken",
    unit: "100gm",
    calories:239,
  },
   {
    name: "Paneer",
    unit: "100gm",
    calories: 296,
  },
  {
    name: "Chana daal",
    unit: "100gm",
    calories: 115,
  },
  {
    name: "Oats",
    unit: "100gm",
    calories: 379,
  },
  {
    name: "Curd",
    unit: "100gm",
    calories: 98,
  },
  {
    name: "Milk",
    unit:"100gm",
    calories:42,
  },
  {
    name: "Egg(boiled)",
    unit: "100gm",
    calories: 155,
  },
  {
    name: "Raw Spinach",
    unit: "100gm",
    calories: 23,
  },
  {
    name: "Fish",
    unit: "100gm",
    calories:206,
  },
  {
    name: "Broccoli",
    unit: "100gm",
    calories: 34,
  },
  {
    name: "Raw Beetroot",
    unit: "100gm",
    calories: 43,
  },
  
];
let exercise = [ 
  { 
    name: "Jumping rope", 
    unit: "min", 
    calories: 18 , 
  },
  { 
    name: "Plank", 
    unit: "min", 
    calories: 4 , 
  }, 
   
  { 
    name: "Squats", 
    unit: "min", 
    calories: 8, 
  },
  { 
    name: "Push-ups", 
    unit:"min", 
    calories: 6 , 
  },   
  { 
    name: "Pull-ups", 
    unit:"min", 
    calories: 7, 
  },
  { 
    name: "Curl-ups", 
    unit: "min", 
    calories: 5 , 
  }, 
  { 
    name: "Lunges", 
    unit: "min", 
    calories: 7 , 
  },
  { 
    name: "Jumping jacks", 
    unit: "min", 
    calories: 8 , 
  },
  { 
    name:"Burpees", 
    unit: "min", 
    calories: 10 , 
  }, 
  { 
    name: "Bicycle crunches", 
    unit: "min", 
    calories: 3 , 
  },
  { 
    name: "High knees", 
    unit: "min", 
    calories: 8 , 
  },
  { 
    name: "Running", 
    unit: "min", 
    calories: 11 , 
  }, 
  { 
    name: "Butt-bridge", 
    unit: "min", 
    calories: 8 , 
  },
  { 
    name: "Mountain climber", 
    unit: "min", 
    calories: 10, 
  },
  { 
    name: "walking", 
    unit: "min", 
    calories: 4 , 
  },
];

let typeOfEntry = document.querySelector("#type");
let entrySelect = document.querySelector(".entrySelect");
let entryName = document.querySelector(".entryName");
let caloriesData = document.querySelector("#caloriesData");
let entryCount = document.querySelector("#entryCount");


let foodHtml = ''
let exerciseHtml = ''

food.forEach(ele => {
  foodHtml += `<option value=${ele.name}>${ele.name} (${ele.unit})</option>`
})

exercise.forEach(ele => {
  exerciseHtml += `<option value=${ele.name}>${ele.name} (${ele.unit})</option>`
})

entryName.innerHTML = foodHtml 
caloriesData.value = food[0].calories * entryCount.value

typeOfEntry.addEventListener("change", () =>
  renderForm(typeOfEntry.selectedOptions[0].getAttribute("value"))
);

entryName.addEventListener("change", () =>
  calculateCal(entryName.selectedOptions[0].getAttribute("value"), entryCount.value)
);

entryCount.addEventListener("change", () =>
  calculateCal(entryName.selectedOptions[0].getAttribute("value"), entryCount.value)
);

let renderForm = (type) => {
  if(type == "Food" || type == "Exercise"){
    document.querySelector('.entries').classList.add("d-block")
    document.querySelector('.entries').classList.remove("d-none")
    document.querySelector('.waterEntry').classList.add("d-none")
    document.querySelector('.waterEntry').classList.remove("d-block")
    entrySelect.innerHTML = "Name of " + type;
    entryName.innerHTML = type == 'Food' ? foodHtml : exerciseHtml
    if(type == "Food"){
      entryCount.value = 1
      caloriesData.value = food[0].calories * entryCount.value
    }else{
      entryCount.value = 1
      caloriesData.value = exercise[0].calories * entryCount.value
    }
  }
  else if(type == "Water"){
  document.querySelector('.entries').classList.add("d-none")
  document.querySelector('.entries').classList.remove("d-block")
  document.querySelector('.waterEntry').classList.add("d-block")
  document.querySelector('.waterEntry').classList.remove("d-none")
  }
};

let calculateCal = (entry, count) => {
  if(typeOfEntry.selectedOptions[0].value == "Food"){ 
    food.forEach(ele => {
      if(ele.name == entry){
        caloriesData.value = ele.calories * count
      }
    })
  }else{
    exercise.forEach(ele => {
      if(ele.name == entry){
        caloriesData.value = ele.calories * count
      }
    })
  }
}