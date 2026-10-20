# Ideation

Planned implementation of the port scheduling software. Diagrams use Mermaid and render on GitHub.

## System Overview

```mermaid
flowchart LR
    subgraph Inputs
        V[Vessel calls<br/>ETA, ETD, LOA, beam,<br/>arrival & departure draft]
        B[Berth data<br/>length, breadth, depth]
        T[Tide data<br/>predicted tide tables]
    end

    subgraph Core
        F[Berth Finder<br/>dimension & draft checks]
        W[Tide Window Calculator<br/>safe entry/exit times]
        S[Scheduler<br/>berth allocation & conflict resolution]
        X[Scenario Simulator<br/>delays / early arrivals]
    end

    subgraph Outputs
        G[Berth timeline<br/>Gantt view]
        R[Schedule reports<br/>for shipping lines & agents]
    end

    V --> F
    B --> F
    T --> W
    V --> W
    F --> S
    W --> S
    S --> X
    X --> S
    S --> G
    S --> R
```

## Scheduling Flow

```mermaid
flowchart TD
    A[New vessel call] --> B[Find berths that fit<br/>length, breadth]
    B --> C{Any berth fits?}
    C -- No --> Z[Reject / flag for review]
    C -- Yes --> D[Compute tide windows where<br/>draft ≤ depth + tide]
    D --> E{Window near ETA?}
    E -- No --> F[Shift to next tide window]
    F --> G
    E -- Yes --> G{Berth free in that slot?}
    G -- No --> H[Try next berth or next slot]
    H --> D
    G -- Yes --> I[Allocate berth slot]
    I --> J[Check departure draft<br/>against tide at ETD]
    J --> K[Add to schedule]
```

## Scenario Simulation

```mermaid
sequenceDiagram
    participant U as Port Planner
    participant S as Scheduler
    participant X as Simulator
    participant R as Reports

    U->>X: Delay vessel A by 6 h
    X->>S: Re-run allocation with new ETA
    S-->>X: Updated schedule + affected vessels
    X-->>U: Show conflicts and waiting times
    U->>R: Export chosen schedule
    R-->>U: PDF / CSV schedule report
```

## Data Model

```mermaid
erDiagram
    VESSEL ||--o{ VESSEL_CALL : makes
    BERTH ||--o{ ALLOCATION : hosts
    VESSEL_CALL ||--o| ALLOCATION : gets
    TIDE_READING }o--|| PORT : "measured at"
    PORT ||--o{ BERTH : has

    VESSEL {
        string name
        float length
        float breadth
    }
    VESSEL_CALL {
        datetime eta
        datetime etd
        float arrival_draft
        float departure_draft
    }
    BERTH {
        string name
        float length
        float breadth
        float depth
    }
    ALLOCATION {
        datetime start
        datetime end
    }
    TIDE_READING {
        datetime time
        float height
    }
```

## Roadmap

```mermaid
flowchart LR
    P1[1. Baseline<br/>Berth Finder] --> P2[2. Tide tables<br/>& tide windows]
    P2 --> P3[3. Multi-vessel<br/>scheduler]
    P3 --> P4[4. Scenario<br/>simulation]
    P4 --> P5[5. Timeline view<br/>& reports]
```
