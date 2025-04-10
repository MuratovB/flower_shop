import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import OrderCancellationForm from './customer/OrderCancellationForm';
import CustomerContactRegistration from './customer/CustomerContactRegistration';
import OrderContactRegistration from './customer/OrderContactRegistration';
import OrderCompositionEdit from './customer/OrderCompositionEdit';
import OrderPaymentForm from './customer/OrderPaymentForm';
import PriceList from './customer/PriceList';
import OrderReceipt from './customer/OrderReceipt';
import CustomerOrders from './customer/CustomerOrders';
import OrderPaymentsReport from './customer/OrderPaymentsReport';
import PromotionsList from './customer/PromotionsList';
import CustomerDebts from './customer/CustomerDebts';
import CancelledOrders from './customer/CancelledOrders';

function CustomerViews() {
  return (
    <div>
      <h2>Customer Portal</h2>
      <nav>
        <Link to="order-cancellation">Order Cancellation</Link>
        <Link to="customer-contact-registration">Customer Contact Registration</Link>
        <Link to="order-contact-registration">Order Contact Registration</Link>
        <Link to="edit-order-composition">Edit Order Composition</Link>
        <Link to="order-payment">Order Payment</Link>
        <Link to="price-list">Price List</Link>
        <Link to="order-receipt">Order Receipt</Link>
        <Link to="customer-orders">My Orders</Link>
        <Link to="order-payments">Order Payments</Link>
        <Link to="promotions">Promotions</Link>
        <Link to="debts">My Debts</Link>
        <Link to="cancelled-orders">Cancelled Orders</Link>
      </nav>

      <Routes>
        <Route path="order-cancellation" element={<OrderCancellationForm />} />
        <Route path="customer-contact-registration" element={<CustomerContactRegistration />} />
        <Route path="order-contact-registration" element={<OrderContactRegistration />} />
        <Route path="edit-order-composition" element={<OrderCompositionEdit />} />
        <Route path="order-payment" element={<OrderPaymentForm />} />
        <Route path="price-list" element={<PriceList />} />
        <Route path="order-receipt" element={<OrderReceipt />} />
        <Route path="customer-orders" element={<CustomerOrders />} />
        <Route path="order-payments" element={<OrderPaymentsReport />} />
        <Route path="promotions" element={<PromotionsList />} />
        <Route path="debts" element={<CustomerDebts />} />
        <Route path="cancelled-orders" element={<CancelledOrders />} />
      </Routes>
    </div>
  );
}

export default CustomerViews;