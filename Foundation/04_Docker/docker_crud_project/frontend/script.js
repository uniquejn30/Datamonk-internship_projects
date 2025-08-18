// frontend/script.js
document.addEventListener('DOMContentLoaded', () => {
    const apiUrl = 'http://localhost:3000/items'; // Backend API URL

    const itemForm = document.getElementById('item-form');
    const itemIdInput = document.getElementById('item-id');
    const itemNameInput = document.getElementById('item-name');
    const itemList = document.getElementById('item-list');
    const submitBtn = document.getElementById('submit-btn');
    const cancelBtn = document.getElementById('cancel-btn');

    let isUpdating = false;

    // --- Helper Functions ---

    // Reset form to its initial state
    const resetForm = () => {
        isUpdating = false;
        itemIdInput.value = '';
        itemNameInput.value = '';
        submitBtn.textContent = 'Add Item';
        cancelBtn.classList.add('hidden');
    };

    // Render items in the list
    const renderItems = (items) => {
        itemList.innerHTML = ''; // Clear current list
        if (items.length === 0) {
            itemList.innerHTML = '<li>No items found.</li>';
            return;
        }
        items.forEach(item => {
            const li = document.createElement('li');
            li.dataset.id = item.id;
            
            li.innerHTML = `
                <span class="item-name">${item.name}</span>
                <div class="actions">
                    <button class="edit-btn">Edit</button>
                    <button class="delete-btn">Delete</button>
                </div>
            `;
            itemList.appendChild(li);
        });
    };

    // --- API Call Functions ---

    // Fetch all items from the backend
    const fetchItems = async () => {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const result = await response.json();
            renderItems(result.data);
        } catch (error) {
            console.error('Failed to fetch items:', error);
            itemList.innerHTML = '<li>Error loading items.</li>';
        }
    };

    // Create a new item
    const createItem = async (name) => {
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name }),
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            await response.json();
            fetchItems(); // Refresh the list
            resetForm();
        } catch (error) {
            console.error('Failed to create item:', error);
        }
    };

    // Update an existing item
    const updateItem = async (id, name) => {
        try {
            const response = await fetch(`${apiUrl}/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name }),
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            await response.json();
            fetchItems(); // Refresh the list
            resetForm();
        } catch (error) {
            console.error('Failed to update item:', error);
        }
    };

    // Delete an item
    const deleteItem = async (id) => {
        try {
            const response = await fetch(`${apiUrl}/${id}`, {
                method: 'DELETE',
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            await response.json();
            fetchItems(); // Refresh the list
        } catch (error) {
            console.error('Failed to delete item:', error);
        }
    };

    // --- Event Listeners ---

    // Handle form submission for creating or updating items
    itemForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const itemName = itemNameInput.value.trim();
        if (!itemName) return;

        if (isUpdating) {
            const itemId = itemIdInput.value;
            updateItem(itemId, itemName);
        } else {
            createItem(itemName);
        }
    });

    // Handle clicks on Edit and Delete buttons
    itemList.addEventListener('click', (e) => {
        const target = e.target;
        const li = target.closest('li');
        if (!li) return;
        
        const itemId = li.dataset.id;

        if (target.classList.contains('delete-btn')) {
            if (confirm('Are you sure you want to delete this item?')) {
                deleteItem(itemId);
            }
        }

        if (target.classList.contains('edit-btn')) {
            isUpdating = true;
            const itemName = li.querySelector('.item-name').textContent;
            itemIdInput.value = itemId;
            itemNameInput.value = itemName;
            submitBtn.textContent = 'Update Item';
            cancelBtn.classList.remove('hidden');
            itemNameInput.focus();
        }
    });

    // Handle cancel button click
    cancelBtn.addEventListener('click', resetForm);

    // --- Initial Load ---
    fetchItems();
});
