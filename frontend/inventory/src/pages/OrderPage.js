import React from "react";
import Table from "../components/Table";

const OrderPage = () => {
  return (
    <div className="order-page">
      <h1>Orders</h1>
      <button>Create New Order</button>
      <Table
        title="Orders"
        data={[
          { id: 1, customer: "John Doe", status: "Shipped", total: "$150" },
          { id: 2, customer: "Jane Smith", status: "Pending", total: "$200" },
        ]}
      />
    </div>
  );
};

export default OrderPage;
