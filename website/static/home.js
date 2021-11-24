let foods = [
  {
    name: "Roti",
    unit: "200gm",
    calories: 120,
  },
  {
    name: "Daal",
    unit: "100gm",
    calories: 110,
  },
];
let exercise = [
  {
    name: "Push ups",
    unit: "10/set",
    calories: 80,
  },
  {
    name: "Pull ups",
    unit: "10/set",
    calories: 110,
  },
];

let typeOfEntry = document.querySelector("#type");
let entryName = document.querySelector(".entryName");

typeOfEntry.addEventListener("change", () =>
  renderForm(typeOfEntry.getAttribute("value"))
);

let renderForm = (type) => {
  entryName.innerHTML = "Name of " + type;
};
