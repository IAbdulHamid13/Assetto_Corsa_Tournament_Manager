from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Admin(Account):
    pass

class Participant(Account):
    pass

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    participants = models.ForeignKey(Participant, related_name='events', on_delete=models.CASCADE)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='events')
    server = models.ForeignKey('Server', on_delete=models.CASCADE, related_name='events')

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

class Server(models.Model):
    # [SERVER]
    name = models.CharField(max_length=255, default='New Server')
    cars = models.CharField(max_length=255)
    config_track = models.CharField(max_length=255)
    track = models.CharField(max_length=255)
    sun_angle = models.IntegerField(default=-16) # This is clear weather, -16 is the default value for clear weather in Assetto Corsa
    password = models.CharField(max_length=255, blank=True, default='')
    admin_password = models.CharField(max_length=255, default='admin')
    udp_port = models.IntegerField(default=9600)
    tcp_port = models.IntegerField(default=9600)
    http_port = models.IntegerField(default=8081)
    max_ballast_kg = models.IntegerField(default=150)
    qualify_max_wait_perc = models.IntegerField(default=120)
    race_pit_window_start = models.IntegerField(default=0)
    race_pit_window_end = models.IntegerField(default=0)
    reversed_grid_race_positions = models.IntegerField(default=0)
    locked_entry_list = models.IntegerField(default=0)
    pickup_mode_enabled = models.IntegerField(default=1)
    loop_mode = models.IntegerField(default=1)
    sleep_time = models.IntegerField(default=1)
    client_send_interval_hz = models.IntegerField(default=18)
    send_buffer_size = models.IntegerField(default=0)
    recv_buffer_size = models.IntegerField(default=0)
    race_over_time = models.IntegerField(default=60)
    kick_quorum = models.IntegerField(default=70)
    voting_quorum = models.IntegerField(default=70)
    vote_duration = models.IntegerField(default=15)
    blacklist_mode = models.IntegerField(default=0)
    fuel_rate = models.IntegerField(default=100)
    damage_multiplier = models.IntegerField(default=0)
    tyre_wear_rate = models.IntegerField(default=100)
    allowed_tyres_out = models.IntegerField(default=2)
    abs_allowed = models.IntegerField(default=1)
    tc_allowed = models.IntegerField(default=1)
    start_rule = models.IntegerField(default=1)
    race_gas_penalty_disabled = models.IntegerField(default=0)
    time_of_day_mult = models.IntegerField(default=1)
    result_screen_time = models.IntegerField(default=10)
    max_contacts_per_km = models.IntegerField(default=5)
    stability_allowed = models.IntegerField(default=0)
    autoclutch_allowed = models.IntegerField(default=1)
    tyre_blankets_allowed = models.IntegerField(default=1)
    force_virtual_mirror = models.IntegerField(default=1)
    register_to_lobby = models.IntegerField(default=1)
    max_clients = models.IntegerField(default=2)
    num_threads = models.IntegerField(default=2)
    udp_plugin_local_port = models.IntegerField(default=0)
    udp_plugin_address = models.CharField(max_length=255, blank=True, default='')
    auth_plugin_address = models.CharField(max_length=255, blank=True, default='')
    legal_tyres = models.CharField(max_length=255, blank=True, default='')
    welcome_message = models.CharField(max_length=255, blank=True, default='')

    # [FTP]
    ftp_host = models.CharField(max_length=255, blank=True, default='')
    ftp_login = models.CharField(max_length=255, blank=True, default='')
    ftp_password = models.CharField(max_length=255, blank=True, default='zEFDkKnFcE7qqha92dxVvQ==')
    ftp_folder = models.CharField(max_length=255, blank=True, default='')
    ftp_linux = models.IntegerField(default=0)

    # [DYNAMIC_TRACK]
    dynamic_track_session_start = models.IntegerField(default=98)
    dynamic_track_randomness = models.IntegerField(default=2)
    dynamic_track_session_transfer = models.IntegerField(default=90)
    dynamic_track_lap_gain = models.IntegerField(default=22)

    # [WEATHER_0]
    weather_graphics = models.CharField(max_length=255, default='3_clear')
    base_temperature_ambient = models.IntegerField(default=20)
    base_temperature_road = models.IntegerField(default=7)
    variation_ambient = models.IntegerField(default=2)
    variation_road = models.IntegerField(default=2)
    wind_base_speed_min = models.IntegerField(default=0)
    wind_base_speed_max = models.IntegerField(default=5)
    wind_base_direction = models.IntegerField(default=45)
    wind_variation_direction = models.IntegerField(default=5)

    # [DATA]
    description = models.CharField(max_length=255, blank=True, default='')
    exserverexe = models.CharField(max_length=255, blank=True, default='')
    exserverbat = models.CharField(max_length=255, blank=True, default='')
    exserverhidewin = models.IntegerField(default=0)
    weblink = models.CharField(max_length=255, blank=True, default='')
    welcome_path = models.CharField(max_length=255, blank=True, default='')

class Car(models.Model):
    # [CAR_0]
    model = models.CharField(max_length=255, blank=True, default='')
    skin = models.CharField(max_length=255, blank=True, default='')
    spectator_mode = models.IntegerField(default=0)
    drivername = models.CharField(max_length=255, blank=True, default='')
    team = models.CharField(max_length=255, blank=True, default='')
    guid = models.CharField(max_length=255, blank=True, default='')
    ballast = models.IntegerField(default=0)
    restrictor = models.IntegerField(default=0)

    def __str__(self):
        return self.model or self.drivername or 'Car'
