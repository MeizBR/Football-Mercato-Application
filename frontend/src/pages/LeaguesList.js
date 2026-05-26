import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import Navbar from "../components/Navbar";
import ClubsBar from "../components/ClubsBar";
import Footer from "../components/Footer";
import {
  Trophy,
  MapPin,
  Users,
  Shield,
  Star,
} from "lucide-react";

const leaguesData = [
  {
    slug: "premier-league",
    name: "Premier League",
    country: "England",
    image:
      "https://images.unsplash.com/photo-1522778119026-d647f0596c20?q=80&w=1200&auto=format&fit=crop",
    description:
      "The Premier League is one of the most competitive and popular football leagues in the world, featuring legendary clubs and world-class players.",
    clubs: [
      "Manchester City",
      "Arsenal",
      "Liverpool",
      "Chelsea",
      "Manchester United",
      "Tottenham",
    ],
  },
  {
    slug: "la-liga",
    name: "La Liga",
    country: "Spain",
    image:
      "https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=1200&auto=format&fit=crop",
    description:
      "La Liga is known for technical football, tactical brilliance, and iconic clubs such as Real Madrid and Barcelona.",
    clubs: [
      "Real Madrid",
      "Barcelona",
      "Atletico Madrid",
      "Sevilla",
      "Real Sociedad",
    ],
  },
  {
    slug: "serie-a",
    name: "Serie A",
    country: "Italy",
    image:
      "https://images.unsplash.com/photo-1518604666860-9ed391f76460?q=80&w=1200&auto=format&fit=crop",
    description:
      "Serie A combines tactical discipline with passionate football culture and historic rivalries.",
    clubs: ["Inter", "Juventus", "Milan", "Napoli", "Roma", "Lazio"],
  },
  {
    slug: "bundesliga",
    name: "Bundesliga",
    country: "Germany",
    image:
      "https://images.unsplash.com/photo-1547347298-4074fc3086f0?q=80&w=1200&auto=format&fit=crop",
    description:
      "The Bundesliga is famous for its attacking football, fan atmosphere, and high-scoring matches.",
    clubs: [
      "Bayern Munich",
      "Borussia Dortmund",
      "Leipzig",
      "Leverkusen",
      "Frankfurt",
    ],
  },
  {
    slug: "ligue-1",
    name: "Ligue 1",
    country: "France",
    image:
      "https://images.unsplash.com/photo-1508098682722-e99c643e7485?q=80&w=1200&auto=format&fit=crop",
    description:
      "Ligue 1 is home to emerging talents and elite football clubs with strong youth development.",
    clubs: ["PSG", "Marseille", "Lyon", "Monaco", "Lille"],
  },
  {
    slug: "eredivisie",
    name: "Eredivisie",
    country: "Netherlands",
    image:
      "https://images.unsplash.com/photo-1486286701208-1d58e9338013?q=80&w=1200&auto=format&fit=crop",
    description:
      "The Eredivisie is recognized for developing young talents and promoting attacking football.",
    clubs: ["Ajax", "PSV", "Feyenoord", "AZ Alkmaar"],
  },
  {
    slug: "liga-nos",
    name: "Liga NOS",
    country: "Portugal",
    image:
      "https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?q=80&w=1200&auto=format&fit=crop",
    description:
      "Portugal’s top league is famous for technical players and producing future global stars.",
    clubs: ["Benfica", "Porto", "Sporting CP", "Braga"],
  },
  {
    slug: "super-lig",
    name: "Süper Lig",
    country: "Turkey",
    image:
      "https://images.unsplash.com/photo-1517927033932-b3d18e61fb3a?q=80&w=1200&auto=format&fit=crop",
    description:
      "The Turkish Süper Lig delivers intense rivalries and electric atmospheres across stadiums.",
    clubs: [
      "Galatasaray",
      "Fenerbahçe",
      "Beşiktaş",
      "Trabzonspor",
    ],
  },
  {
    slug: "jupiler-pro-league",
    name: "Jupiler Pro League",
    country: "Belgium",
    image:
      "https://images.unsplash.com/photo-1517466787929-bc90951d0974?q=80&w=1200&auto=format&fit=crop",
    description:
      "Belgium’s top division is known for discovering and developing elite young players.",
    clubs: ["Club Brugge", "Anderlecht", "Genk", "Gent"],
  },
  {
    slug: "allsvenskan",
    name: "Allsvenskan",
    country: "Sweden",
    image:
      "https://images.unsplash.com/photo-1508098682722-e99c643e7485?q=80&w=1200&auto=format&fit=crop",
    description:
      "Sweden’s top football division offers exciting local rivalries and passionate supporters.",
    clubs: ["Malmö FF", "AIK", "Djurgårdens IF", "Hammarby"],
  },
  {
    slug: "eliteserien",
    name: "Eliteserien",
    country: "Norway",
    image:
      "https://images.unsplash.com/photo-1459865264687-595d652de67e?q=80&w=1200&auto=format&fit=crop",
    description:
      "Norway’s premier league features energetic football and strong Scandinavian talent.",
    clubs: ["Bodø/Glimt", "Molde", "Rosenborg", "Brann"],
  },
  {
    slug: "super-league",
    name: "Swiss Super League",
    country: "Switzerland",
    image:
      "https://images.unsplash.com/photo-1517927033932-b3d18e61fb3a?q=80&w=1200&auto=format&fit=crop",
    description:
      "The Swiss Super League mixes experienced clubs with exciting emerging players.",
    clubs: ["Young Boys", "Basel", "Zurich", "Lugano"],
  },
  {
    slug: "superliga",
    name: "Danish Superliga",
    country: "Denmark",
    image:
      "https://images.unsplash.com/photo-1522778119026-d647f0596c20?q=80&w=1200&auto=format&fit=crop",
    description:
      "Denmark’s Superliga is competitive, fast-paced, and known for developing Scandinavian talent.",
    clubs: ["Copenhagen", "Midtjylland", "Brøndby", "Nordsjælland"],
  },
];

export default function LeaguesList() {
  return (
    <>
    <Header />
    <Navbar />
    <ClubsBar />


    <div className="min-h-screen bg-zinc-950 text-white p-8">
      {/* Header */}
      <div className="max-w-7xl mx-auto mb-12">
        <div className="flex items-center gap-3 mb-4">
          <Trophy className="w-10 h-10 text-yellow-400" />
          <h1 className="text-5xl font-black tracking-tight">
            European Football Leagues
          </h1>
        </div>

        <p className="text-zinc-400 text-lg max-w-3xl">
          Explore the biggest football leagues in Europe, discover their
          history, atmosphere, and the clubs that make them legendary.
        </p>
      </div>

      {/* League Cards */}
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
        {leaguesData.map((league) => (
          <div
            key={league.slug}
            className="bg-zinc-900 rounded-3xl overflow-hidden border border-zinc-800 hover:border-yellow-500/40 transition-all duration-300 hover:scale-[1.02] shadow-2xl"
          >
            {/* Image */}
            <div className="relative h-56 overflow-hidden">
              <img
                src={league.image}
                alt={league.name}
                className="w-full h-full object-cover"
              />

              <div className="absolute inset-0 bg-gradient-to-t from-black via-black/30 to-transparent" />

              <div className="absolute bottom-4 left-4">
                <h2 className="text-3xl font-bold">{league.name}</h2>

                <div className="flex items-center gap-2 text-zinc-200 mt-1">
                  <MapPin className="w-4 h-4" />
                  <span>{league.country}</span>
                </div>
              </div>
            </div>

            {/* Content */}
            <div className="p-6">
              <p className="text-zinc-300 leading-relaxed mb-6">
                {league.description}
              </p>

              <div className="flex items-center gap-2 mb-4">
                <Shield className="w-5 h-5 text-yellow-400" />
                <h3 className="text-lg font-semibold">
                  Popular Clubs
                </h3>
              </div>

              <div className="flex flex-wrap gap-3">
                {league.clubs.map((club) => (
                  <div
                    key={club}
                    className="bg-zinc-800 border border-zinc-700 px-4 py-2 rounded-full text-sm hover:bg-yellow-500 hover:text-black transition-all duration-200 cursor-pointer flex items-center gap-2"
                  >
                    <Star className="w-3 h-3" />
                    {club}
                  </div>
                ))}
              </div>

              {/* Footer */}
              <div className="mt-6 pt-5 border-t border-zinc-800 flex items-center justify-between">
                <div className="flex items-center gap-2 text-zinc-400">
                  <Users className="w-4 h-4" />
                  <span>{league.clubs.length} Clubs Highlighted</span>
                </div>

                <button className="bg-yellow-400 text-black font-semibold px-4 py-2 rounded-xl hover:bg-yellow-300 transition">
                  Explore
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>


    <Footer />
    </>
  );
}