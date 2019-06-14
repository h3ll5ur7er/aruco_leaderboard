using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Windows.Documents;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace UserInterface
{
    public class APIViewModel : ViewModel
    {
        private string basePath = "http://localhost:5000";
        private DefaultApi api = null;
        private ObservableCollection<Team> _teams;
        private ObservableCollection<Driver> _drivers;
        private ObservableCollection<Result> _results;
        private ObservableCollection<Lap> _laps;
        private ObservableCollection<Race> _races;
        private ObservableCollection<Event> _events;
        private ObservableCollection<Category> _categories;

        public APIViewModel()
        {
            DoFetchAll(null);
        }

        public ObservableCollection<Team> Teams
        {
            get => _teams;
            set => Set(ref _teams, value);
        }

        public ObservableCollection<Driver> Drivers
        {
            get => _drivers;
            set => Set(ref _drivers, value);
        }

        public ObservableCollection<Category> Categories
        {
            get => _categories;
            set => Set(ref _categories, value);
        }

        public ObservableCollection<Event> Events
        {
            get => _events;
            set => Set(ref _events, value);
        }

        public ObservableCollection<Race> Races
        {
            get => _races;
            set => Set(ref _races, value);
        }

        public ObservableCollection<Lap> Laps
        {
            get => _laps;
            set => Set(ref _laps, value);
        }

        public ObservableCollection<Result> Results
        {
            get => _results;
            set => Set(ref _results, value);
        }
        
        public RelayCommand FetchAll => new RelayCommand(DoFetchAll);
        private void DoFetchAll(object param)
        {
            if(api == null)
                api = new DefaultApi();
            Teams.Clear();
            foreach (var team in api.GetAllTeamsEndpoint()._Teams)
            {
                Teams.Add(team);
            }
            Drivers.Clear();
            foreach (var driver in api.GetAllDriversEndpoint()._Drivers)
            {
                Drivers.Add(driver);
            }
            Categories.Clear();
            foreach (var category in api.GetAllCategoriesEndpoint()._Categories)
            {
                Categories.Add(category);
            }
            Events.Clear();
            foreach (var _event in api.GetAllEventsEndpoint()._Events)
            {
                Events.Add(_event);
            }
            Races.Clear();
            foreach (var race in api.GetAllRacesEndpoint()._Races)
            {
                Races.Add(race);
            }
            Laps.Clear();
            foreach (var lap in api.GetAllLapEndpoint()._Laps)
            {
                Laps.Add(lap);
            }
            Results.Clear();
            foreach (var result in api.GetAllResultsEndpoint()._Results)
            {
                Results.Add(result);
            }
        }
    }
}