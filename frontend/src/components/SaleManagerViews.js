import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import OrderEditForm from './sales/OrderEditForm';
import OrderCancellationForm from './sales/OrderCancellationForm';
import SalesByProduct from './sales/SalesByProduct';
import OrdersList from './sales/OrdersList';
import CustomerDebts from './sales/CustomerDebts';
import WarehouseStock from './sales/WarehouseStock';
import PromotionsList from './sales/PromotionsList';
import SalesByCustomer from './sales/SalesByCustomer';
import SalesByWarehouse from './sales/SalesByWarehouse';
import OrderComposition from './sales/OrderComposition';
import CancelledOrders from './sales/CancelledOrders';
import SalesByRegion from './sales/SalesByRegion';
import SalesByBusinessType from './sales/SalesByBusinessType';
import SalesByEvents from './sales/SalesByEvents';

function SalesManagerViews() {
  return (
    <div>
      <h2>Sales Manager Portal</h2>
      <nav>
        <Link to="edit-order">Edit Order</Link>
        <Link to="cancel-order">Cancel Order</Link>
        <Link to="sales-by-product">Sales by Product</Link>
        <Link to="orders">Orders</Link>
        <Link to="customer-debts">Customer Debts</Link>
        <Link to="warehouse-stock">Warehouse Stock</Link>
        <Link to="promotions">Promotions</Link>
        <Link to="sales-by-customer">Sales by Customer</Link>
        <Link to="sales-by-warehouse">Sales by Warehouse</Link>
        <Link to="order-composition">Order Composition</Link>
        <Link to="cancelled-orders">Cancelled Orders</Link>
        <Link to="sales-by-region">Sales by Region</Link>
        <Link to="sales-by-business">Sales by Business Type</Link>
        <Link to="sales-by-events">Sales by Events</Link>
      </nav>

      <Routes>
        <Route path="edit-order" element={<OrderEditForm />} />
        <Route path="cancel-order" element={<OrderCancellationForm />} />
        <Route path="sales-by-product" element={<SalesByProduct />} />
        <Route path="orders" element={<OrdersList />} />
        <Route path="customer-debts" element={<CustomerDebts />} />
        <Route path="warehouse-stock" element={<WarehouseStock />} />
        <Route path="promotions" element={<PromotionsList />} />
        <Route path="sales-by-customer" element={<SalesByCustomer />} />
        <Route path="sales-by-warehouse" element={<SalesByWarehouse />} />
        <Route path="order-composition" element={<OrderComposition />} />
        <Route path="cancelled-orders" element={<CancelledOrders />} />
        <Route path="sales-by-region" element={<SalesByRegion />} />
        <Route path="sales-by-business" element={<SalesByBusinessType />} />
        <Route path="sales-by-events" element={<SalesByEvents />} />
      </Routes>
    </div>
  );
}

export default SalesManagerViews;