import React, { useState, useEffect } from 'react';
import Table from '../components/Table';
import FormModal from '../components/FormModal';

const InventoryPage = () => {
    const [inventoryItems, setInventoryItems] = useState([]);
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        // Fetch inventory items from backend API
        fetch('/api/inventory/')
            .then(response => response.json())
            .then(data => setInventoryItems(data));
    }, []);

    const handleAddItem = () => {
        setShowModal(true);
    };

    return (
        <div className="inventory">
            <h1>Inventory</h1>
            <button onClick={handleAddItem}>Add New Item</button>
            <Table data={inventoryItems} columns={['Name', 'Quantity', 'Supplier', 'Price']} />
            {showModal && <FormModal onClose={() => setShowModal(false)} />}
        </div>
    );
};

export default InventoryPage;
