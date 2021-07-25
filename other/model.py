# generated by datamodel-codegen:
#   filename:  test.json
#   timestamp: 2021-07-25T13:00:30+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class OrderDetails(BaseModel):
    order_id: str
    order_datetime: str
    order_shipping_price_gross: Any
    order_additional_information: str


class PatientDetail(BaseModel):
    patient_id: int
    gender: str
    firstname: str
    lastname: str
    email: str
    phone: str
    date_of_birth: str
    insurance_name: str
    insurance_identifier: str
    patient_insurance_number: str
    exempt_from_additional_charges: bool


class CustomerDetails(BaseModel):
    gender: str
    firstname: str
    lastname: str
    email: str
    phone: str
    date_of_birth: str


class DeliveryAddress(BaseModel):
    gender: str
    firstname: str
    lastname: str
    company: str
    street_name: str
    street_number: str
    city: str
    postcode: str
    country: str
    country_iso_code: str
    additional_address_information: str


class BillingAddress(BaseModel):
    gender: str
    firstname: str
    lastname: str
    company: str
    street_name: str
    street_number: str
    city: str
    postcode: str
    country: str
    country_iso_code: str
    additional_address_information: str


class NursingHomeAddress(BaseModel):
    nursing_home_number: str
    company: str
    email: str
    phone: str
    street_name: str
    street_number: str
    city: str
    postcode: str
    country: str
    country_iso_code: str
    additional_address_information: str


class PatientsProductsDetail(BaseModel):
    patient_id: str
    prescription_id: str
    product_token: str
    quantity: int
    additional_payment: bool
    additional_payment_amount_net: float
    aut_idem: bool


class Product(BaseModel):
    pzn: str
    ntin: str
    name: str
    total_quantity: str
    patients_products_details: List[PatientsProductsDetail]
    unit_price_net: float
    tax_rate: float


class RecognitionRates(BaseModel):
    products: float
    patient_details: float
    prescription: float


class Prescription(BaseModel):
    prescription_id: str
    prescription_token: str
    prescription_type: str
    prescription: str
    format: Any
    mime_type: str
    permanent_establishment_number: Any
    doctor_number: Any
    date_of_exhibition: Any
    recognition_rates: RecognitionRates


class Model(BaseModel):
    order_details: OrderDetails
    patient_details: List[PatientDetail]
    customer_details: CustomerDetails
    delivery_address: DeliveryAddress
    billing_address: BillingAddress
    nursing_home_address: NursingHomeAddress
    products: List[Product]
    prescriptions: List[Prescription]
