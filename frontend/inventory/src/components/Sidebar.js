import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => (
    <aside className="sidebar">
        <ul>
            <li><Link to="/dashboard">Dashboard</Link></li>
            <li><Link to="/inventory">Inventory</Link></li>
            <li><Link to="/orders">Orders</Link></li>
            <li><Link to="/suppliers">Suppliers</Link></li>
            <li><Link to="/reports">Reports</Link></li>
        </ul>
    </aside>
);

export default Sidebar;
