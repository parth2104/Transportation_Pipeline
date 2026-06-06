# Transportation Analytics Pipeline using Databricks DLT

## Overview

This project implements an end-to-end Transportation Analytics Pipeline for a ride-sharing company similar to Uber. The objective is to transform continuously arriving operational trip data into reliable, analytics-ready datasets using Databricks Delta Live Tables (DLT) and Medallion Architecture.

The pipeline processes transportation data through Bronze, Silver, and Gold layers, enabling incremental ingestion, data quality enforcement, historical tracking, and business-ready reporting.

## Business Problem

Ride-sharing platforms generate large volumes of trip and city-level operational data. Analysts require clean, trusted, and continuously updated datasets to monitor business performance, customer experience, revenue trends, and operational efficiency.

To address these requirements, this project implements:

* Incremental data processing
* Change Data Capture (CDC)
* Slowly Changing Dimensions (SCD Type 1 & Type 2)
* Medallion Architecture
* Automated data transformation using Delta Live Tables

## Architecture

Raw Source Data
│
▼
Bronze Layer
(Raw Ingestion)
│
▼
Silver Layer
(Cleansing & Business Transformations)
│
▼
Gold Layer
(Analytical Views & CDC Outputs)


## Data Sources

### City Dimension Table

Contains information about operating cities.

### Trip Fact Table

Contains ride-level transactional data including:

* Trip details
* Passenger information
* Distance travelled
* Fare amount
* Customer ratings
* Driver ratings

## Bronze Layer

Purpose:

* Raw data ingestion
* Schema preservation
* Initial validation

Implementation:

* Materialized Views
* Incremental ingestion

## Silver Layer

Purpose:

* Data cleansing
* Standardization
* Business-rule transformations

Implementation:

* Materialized Views
* Data quality checks
* Enrichment and normalization

## Gold Layer

Purpose:

* Business-ready analytical datasets
* Historical tracking
* Reporting consumption

Implementation:

* Analytical Views
* CDC Processing
* SCD Type 1
* SCD Type 2

## Technologies Used

* Databricks
* Delta Live Tables (DLT)
* Delta Lake
* SQL
* CDC
* SCD Type 1 & Type 2
* Medallion Architecture
* Materialized Views

## Key Features

* Declarative Data Pipelines
* Incremental Processing
* Timestamp-Based Loading
* Automated CDC
* Historical Data Tracking
* Business-Focused Transformations
* Analytics-Ready Gold Layer
