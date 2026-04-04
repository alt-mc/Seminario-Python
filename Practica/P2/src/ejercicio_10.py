def competition_simulation(competition_rounds):
    chef_stats = {}

    # cada ronda
    for i, round_data in enumerate(competition_rounds):
        print(f"Ronda {i + 1} : {round_data['theme']}: ")

        # guardo los puntos de cada cocinero en esta ronda
        round_points = {}

        # ptj de cada cocinero en esta ronda
        for chef, judges in round_data["scores"].items():
            # chef nuevo
            if chef not in chef_stats:
                chef_stats[chef] = {
                    "total_points": 0,
                    "rounds_won": 0,
                    "best_round": 0,
                    "played_rounds": 0,
                }

            # sumar nota de los jueces
            curr_points = sum(judges.values())
            round_points[chef] = curr_points

            # actualizar global
            chef_stats[chef]["total_points"] += curr_points
            chef_stats[chef]["played_rounds"] += 1

            if curr_points > chef_stats[chef]["best_round"]:
                chef_stats[chef]["best_round"] = curr_points

        # ganador de la ronda
        max_round_point = max(round_points.values())

        # otra forma era con list comprehension
        round_winners = []
        for c, p in round_points.items():
            if p == max_round_point:
                round_winners.append(c)

        # actualizar el contador
        for w in round_winners:
            chef_stats[w]["rounds_won"] += 1

        names_in_round = ", ".join(round_winners)
        print(f"Ganador: {names_in_round} ({max_round_point} pts)")

        # tabla de posiciones de la ronda
        pts = sorted(round_points.items(), key=lambda x: x[1], reverse=True)

        for chef, points in pts:
            print(f"  {chef}: {points} pts")
        print("-" * 30)

    print("\n")
    print("Tabla de posiciones final:")
    print(
        f"{'Cocinero'} | {'Puntaje'} | {'Rondas ganadas'} | {'Mejor ronda'} | {'Promedio'}"
    )
    print("-" * 65)

    results = []
    for chef, data in chef_stats.items():
        average = data["total_points"] / data["played_rounds"]
        results.append(
            {
                "name": chef,
                "total_points": data["total_points"],
                "rounds_won": data["rounds_won"],
                "best_round": data["best_round"],
                "average": average,
            }
        )

    results.sort(key=lambda x: x["total_points"], reverse=True)

    for res in results:
        print(
            f"{res['name']} | {res['total_points']} | {res['rounds_won']} | {res['best_round']} | {res['average']}"
        )
