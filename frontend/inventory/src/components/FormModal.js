import React, { useState } from "react";

const FormModal = ({ onClose, onSubmit }) => {
  const [formData, setFormData] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
    onClose();
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <h2>Add New Item</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Name:
            <input type="text" name="name" onChange={handleChange} />
          </label>
          <label>
            Quantity:
            <input type="number" name="quantity" onChange={handleChange} />
          </label>
          <label>
            Supplier:
            <input type="text" name="supplier" onChange={handleChange} />
          </label>
          <label>
            Price:
            <input type="number" name="price" onChange={handleChange} />
          </label>
          <button type="submit">Submit</button>
        </form>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default FormModal;
