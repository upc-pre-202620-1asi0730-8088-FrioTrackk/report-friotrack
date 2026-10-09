workspace "FrioTrack" "Current TB1 containers and planned evolution" {
  model {
    user = person "Coordinator or Cargo Client" "Uses an authenticated account"
    maps = softwareSystem "OpenStreetMap" "External map tiles"
    system = softwareSystem "FrioTrack" {
      landing = container "Landing Page" "Public proposal and entry links" "HTML CSS JavaScript / Azure Storage"
      frontend = container "Web Application" "Authenticated shipment views" "Vue PrimeVue / Azure Storage"
      api = container "Supporting API" "Accounts, role authorization and commands" "ASP.NET Core C# / Azure App Service"
      store = container "Private store" "Single-instance persisted state" "JSON / HOME/data"
      database = container "Relational database (planned)" "Target backend design" "PostgreSQL / EF Core"
    }
    user -> landing "Reads proposal"
    user -> frontend "Uses account"
    landing -> frontend "Opens role and language entry link"
    frontend -> api "Authenticates and sends authorized requests" "HTTPS JSON / opaque bearer token"
    frontend -> maps "Loads map tiles" "HTTPS"
    api -> store "Reads and persists accepted state"
    api -> database "Planned migration"
  }
  views {
    container system "Containers" {
      include *
      autoLayout tb
    }
    styles {
      element "Element" { color #142b45 background #e0f2fe }
    }
  }
}
