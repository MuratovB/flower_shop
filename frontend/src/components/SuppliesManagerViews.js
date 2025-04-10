import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import SupplyEditForm from './supplies/SupplyEditForm';
import RegistrationForm from './supplies/RegistrationForm';
import DebtsToSuppliers from './supplies/DebtsToSuppliers';
import SuppliersDebts from './supplies/SuppliersDebts';
import WarehouseList from './supplies/WarehouseList';
import WarehouseStockList from './supplies/WarehouseStockList';
import DefectiveGoodsList from './supplies/DefectiveGoodsList';
import SuppliesByWarehouse from './supplies/SuppliesByWarehouse';
import SuppliesByProduct from './supplies/SuppliesByProduct';
import SuppliesBySupplier from './supplies/SuppliesBySupplier';
import SupplyPayments from './supplies/SupplyPayments';

function SuppliesManagerViews() {
  return (
    <div>
      <h2>Supplies Manager Portal</h2>
      <nav>
        <Link to="edit-supply">Edit Supply</Link>
        <Link to="registration">Registration</Link>
        <Link to="debts-to-suppliers">Debts to Suppliers</Link>
        <Link to="suppliers-debts">Suppliers' Debts</Link>
        <Link to="warehouse-list">Warehouse List</Link>
        <Link to="warehouse-stock">Warehouse Stock</Link>
        <Link to="defective-goods">Defective Goods</Link>
        <Link to="supplies-by-warehouse">Supplies by Warehouse</Link>
        <Link to="supplies-by-product">Supplies by Product</Link>
        <Link to="supplies-by-supplier">Supplies by Supplier</Link>
        <Link to="supply-payments">Supply Payments</Link>
      </nav>

      <Routes>
        <Route path="edit-supply" element={<SupplyEditForm />} />
        <Route path="registration" element={<RegistrationForm />} />
        <Route path="debts-to-suppliers" element={<DebtsToSuppliers />} />
        <Route path="suppliers-debts" element={<SuppliersDebts />} />
        <Route path="warehouse-list" element={<WarehouseList />} />
        <Route path="warehouse-stock" element={<WarehouseStockList />} />
        <Route path="defective-goods" element={<DefectiveGoodsList />} />
        <Route path="supplies-by-warehouse" element={<SuppliesByWarehouse />} />
        <Route path="supplies-by-product" element={<SuppliesByProduct />} />
        <Route path="supplies-by-supplier" element={<SuppliesBySupplier />} />
        <Route path="supply-payments" element={<SupplyPayments />} />
      </Routes>
    </div>
  );
}

export default SuppliesManagerViews;