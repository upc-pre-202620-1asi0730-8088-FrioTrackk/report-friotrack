workspace "FrioTrack" "TB1 implemented architecture" {
  model {
    coordinator = person "Logistics Coordinator" "Schedules shipments and manages resources"
    client = person "Cargo Client" "Consults assigned shipments"
    visitor = person "Visitor" "Reads the product proposal"
    maps = softwareSystem "OpenStreetMap" "External map tile service"
    friotrack = softwareSystem "FrioTrack" {
      web = container "Web Application" "Serves /landing/, index.html and the SPA bundle; does not execute Vue" "Azure Storage Static Website"
      spa = container "Single Page Application" "Runs in the user browser; authenticated views" "Vue 3 PrimeVue JavaScript"
      api = container "Supporting API" "Authenticates, authorizes and validates commands" "ASP.NET Core 10 C#"
      store = container "Private state store" "Single-instance accounts sessions and workspace" "JSON file"
    }
    visitor -> web "Reads /landing/ and follows the application CTA" "HTTPS"
    coordinator -> web "Requests page" "HTTPS"
    client -> web "Requests page" "HTTPS"
    web -> spa "Delivers application" "HTML JavaScript CSS / HTTPS"
    coordinator -> spa "Uses interactive views"
    client -> spa "Uses assigned shipment views"
    spa -> api "Authenticates and executes commands" "HTTPS JSON / opaque bearer token"
    spa -> maps "Loads map tiles" "HTTPS"
    api -> store "Reads and persists accepted state" "Local file I/O"
  }
  views {
    systemContext friotrack "Context" {
      include *
      autoLayout lr
    }
    container friotrack "Containers" {
      include *
      autoLayout tb
    }
    styles {
      element "Person" {
        shape Person
        background #e5e7eb
        color #142b45
      }
      element "Container" {
        background #e0f2fe
        color #142b45
      }
    }
  }
}
