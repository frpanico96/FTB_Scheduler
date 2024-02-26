# FTB Scheduler

<span style="font-size: 1.8em">
Your best friend tournament management app.
</span>

### Table of contents

- [Introduction](#introduction)
- [Description](#description)
- [Technical Details](#technical-details)
  - [Frontend](#frontend)
  - [Backend](#backend)

## Introduction

If you are tired of using tons of paper to manage your tournaments, if you want to organize a large-scale tournament, **FTB Scheduler** is the app for you.

The app allows users to create their own tournament and manage them, chosing the tournament format they think best fits their tournament, inputs results or simulates them if needed.

This app is thought to be used only by tournament manager but it is possible to generate a public link where partecipants can use to track torunament progress and, for instance, incoming match

## Description

## Technical Details

This githtub repos holds both the frontend and the backend of the application in the dedicated folders.

The following technologies have been used to implement the application:

- Frontend: SwiftUI
- Backend: Django framework (Python)

### Frontend

### Backend

The backend architecture is based on microservices each of one perform a specific task:

- **UserDetail Service**: to handle log-in and user registrations
- **Log Service**: centralized service to log every meaningful event on the application
- **Schheduler Service**: handle all the logic for tournament creation and management
- **Simulation Service**: a simulation service which can simulates match (main idea is to use machine learning to achieve the task)
- **Email Service**: to handle email verification, newsletter, notification exc.
