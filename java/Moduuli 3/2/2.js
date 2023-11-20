const targetElement = document.getElementById("target");
const items = [
    "First item", "Second item", "Third item"
]

const list = document.createElement("ul")

for (let i = 0; i < items.length; i++) {
    const item = document.createElement("li");
    item.textContent = items[i];
    if (i === 1) {
    item.classList.add("my-item")
    }
    list.appendChild(item);
}

targetElement.appendChild(list);
