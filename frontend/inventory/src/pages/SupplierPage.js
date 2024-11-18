import React from "react";
import Table from "../components/Table";
import FormModal from "../components/FormModal";

const SuppliersPage = () => {
  return (
    <div className="suppliers-page">
      <h1>Suppliers</h1>
      <button>Add New Supplier</button>
      <FormModal
        title="Add Supplier"
        fields={[
          { name: "Name", type: "text" },
          { name: "Contact", type: "text" },
          { name: "Email", type: "email" },
        ]}
      />
      <Table
        title="Supplier List"
        data={[
          { id: 1, name: "AutoMart", contact: "123456789", email: "info@automart.com" },
          { id: 2, name: "OilWorks", contact: "987654321", email: "sales@oilworks.com" },
        ]}
      />
    </div>
  );
};

export default SuppliersPage;
