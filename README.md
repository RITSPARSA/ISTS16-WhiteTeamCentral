# ISTS16-WhiteTeamCentral

Centralized WhiteTeam backend API for gathering relevant information.

## Status Functions

### Alerts

```
/status/alerts
```
Returns any currently active White Team alerts.

Return Format:
```
{
  'status': 200,
  'alerts': ['Perk5 will be unavailable for 10 minutes']
}
```

### King of the Hill

```
/status/koth
```
Returns status information for King of the Hill.

Return Format:
```
{
  'status': 200,
  'planets': {'planet1': 'team4', 'planet2': 'team1'}
}
```

## Team Functions

### Credits

```
/credits/<teamID>
```
Retrieves the number of credits the given team currently owns.

Return Format:
```
{
  'status': 200,
  'credits': 50000
}
```

### Ships

```
/ships/<teamID>
```
Retrieves the number of ships of each type that the given team currently owns.

Return Format:
```
{
  'status': 200,
  'ship1_count': 50,
  'ship2_count': 0,
  'ship3_count': 1000
}
```

### Stats

```
/stats/<teamID>
```
Retrieves the ship stats that the given team currently has.

Return Format:
```
{
  'status': 200,
  'health': '-50%',
  'damage': '100%',
  'speed': '+100%'
}
```


