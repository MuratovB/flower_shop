import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import WarehouseTurnover from './accountant/WarehouseTurnover';
import BranchTurnover from './accountant/BranchTurnover';
import TotalTurnover from './accountant/TotalTurnover';
import ProductTurnover from './accountant/ProductTurnover';
import ProductCategoryTurnover from './accountant/ProductCategoryTurnover';
import SalesByWarehouse from './accountant/SalesByWarehouse';
import SalesByProductType from './accountant/SalesByProductType';
import SalesByProduct from './accountant/SalesByProduct';
import SalesByBranch from './accountant/SalesByBranch';
import SalesByCustomer from './accountant/SalesByCustomer';
import OrderComposition from './accountant/OrderComposition';
import CancelledOrders from './accountant/CancelledOrders';
import SalesByEmployee from './accountant/SalesByEmployee';
import SalesByPaymentType from './accountant/SalesByPaymentType';
import SuppliesByProductType from './accountant/SuppliesByProductType';
import SuppliesByProduct from './accountant/SuppliesByProduct';
import SuppliesByWarehouse from './accountant/SuppliesByWarehouse';
import SuppliesBySupplier from './accountant/SuppliesBySupplier';
import CustomerDebts from './accountant/CustomerDebts';
import DebtsToSuppliers from './accountant/DebtsToSuppliers';
import SuppliersDebts from './accountant/SuppliersDebts';
import ProductProfitability from './accountant/ProductProfitability';
import BreakEvenPoint from './accountant/BreakEvenPoint';
import Taxes from './accountant/Taxes';
import EmployeeSalaries from './accountant/EmployeeSalaries';
import SalesByPromotions from './accountant/SalesByPromotions';
import ProfitLossReport from './accountant/ProfitLossReport';

function AccountantViews() {
  return (
    <div>
      <h2>Accountant Portal</h2>
      <nav>
        <Link to="warehouse-turnover">Warehouse Turnover</Link>
        <Link to="branch-turnover">Branch Turnover</Link>
        <Link to="total-turnover">Total Turnover</Link>
        <Link to="product-turnover">Product Turnover</Link>
        <Link to="category-turnover">Category Turnover</Link>
        <Link to="sales-by-warehouse">Sales by Warehouse</Link>
        <Link to="sales-by-product-type">Sales by Product Type</Link>
        <Link to="sales-by-product">Sales by Product</Link>
        <Link to="sales-by-branch">Sales by Branch</Link>
        <Link to="sales-by-customer">Sales by Customer</Link>
        <Link to="order-composition">Order Composition</Link>
        <Link to="cancelled-orders">Cancelled Orders</Link>
        <Link to="sales-by-employee">Sales by Employee</Link>
        <Link to="sales-by-payment">Sales by Payment Type</Link>
        <Link to="supplies-by-product-type">Supplies by Product Type</Link>
        <Link to="supplies-by-product">Supplies by Product</Link>
        <Link to="supplies-by-warehouse">Supplies by Warehouse</Link>
        <Link to="supplies-by-supplier">Supplies by Supplier</Link>
        <Link to="customer-debts">Customer Debts</Link>
        <Link to="debts-to-suppliers">Debts to Suppliers</Link>
        <Link to="suppliers-debts">Suppliers' Debts</Link>
        <Link to="product-profitability">Product Profitability</Link>
        <Link to="break-even">Break-even Point</Link>
        <Link to="taxes">Taxes</Link>
        <Link to="salaries">Employee Salaries</Link>
        <Link to="sales-by-promotions">Sales by Promotions</Link>
        <Link to="profit-loss">Profit & Loss Report</Link>
      </nav>

      <Routes>
        <Route path="warehouse-turnover" element={<WarehouseTurnover />} />
        <Route path="branch-turnover" element={<BranchTurnover />} />
        <Route path="total-turnover" element={<TotalTurnover />} />
        <Route path="product-turnover" element={<ProductTurnover />} />
        <Route path="category-turnover" element={<ProductCategoryTurnover />} />
        <Route path="sales-by-warehouse" element={<SalesByWarehouse />} />
        <Route path="sales-by-product-type" element={<SalesByProductType />} />
        <Route path="sales-by-product" element={<SalesByProduct />} />
        <Route path="sales-by-branch" element={<SalesByBranch />} />
        <Route path="sales-by-customer" element={<SalesByCustomer />} />
        <Route path="order-composition" element={<OrderComposition />} />
        <Route path="cancelled-orders" element={<CancelledOrders />} />
        <Route path="sales-by-employee" element={<SalesByEmployee />} />
        <Route path="sales-by-payment" element={<SalesByPaymentType />} />
        <Route path="supplies-by-product-type" element={<SuppliesByProductType />} />
        <Route path="supplies-by-product" element={<SuppliesByProduct />} />
        <Route path="supplies-by-warehouse" element={<SuppliesByWarehouse />} />
        <Route path="supplies-by-supplier" element={<SuppliesBySupplier />} />
        <Route path="customer-debts" element={<CustomerDebts />} />
        <Route path="debts-to-suppliers" element={<DebtsToSuppliers />} />
        <Route path="suppliers-debts" element={<SuppliersDebts />} />
        <Route path="product-profitability" element={<ProductProfitability />} />
        <Route path="break-even" element={<BreakEvenPoint />} />
        <Route path="taxes" element={<Taxes />} />
        <Route path="salaries" element={<EmployeeSalaries />} />
        <Route path="sales-by-promotions" element={<SalesByPromotions />} />
        <Route path="profit-loss" element={<ProfitLossReport />} />
      </Routes>
    </div>
  );
}

export default AccountantViews;