document.addEventListener("change", function (e) {
    if (e.target.classList.contains("checkbox")) {
        const text = e.target.nextElementSibling;
        text.classList.toggle("completed");
    }
});
document.addEventListener("click", function (d) {
    const btn = d.target.closest(".delete")
    if (!btn)
        return;
    const task = btn.parentElement;
    task.remove();
});


document.querySelector(".form").addEventListener("submit", function (e) {
    e.preventDefault(); 
    const input = document.querySelector(".input");
    const value = input.value.trim(); 
    if (value === "") return; 

    const li = document.createElement("li");
    li.classList.add("todoitem");

    const div = document.createElement("div");
    div.classList.add("txt");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.classList.add("checkbox");

    const span = document.createElement("span");
    span.textContent = value;

    div.appendChild(checkbox);
    div.appendChild(span);

    const btn = document.createElement("button");
    btn.type = "button";
    btn.classList.add("delete");
    btn.innerHTML = '<i class="fas fa-trash"></i>';

    li.appendChild(div);
    li.appendChild(btn);

    document.querySelector(".todolist").appendChild(li);
    input.value = "";
});
