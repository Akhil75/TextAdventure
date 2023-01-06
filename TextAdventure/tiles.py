import army, kingdoms, actions, world, player
 
class Westroes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves


class Essos(Westroes):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You are true born of the Targareyan and fighting for the legitamacy to be the 
        heir of the Lord of the seven kingdoms.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class TreasureArea(Westroes):
    def __init__(self, x, y, army):
        self.army = army
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.army)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyKingdom(Westroes):
    def __init__(self, x, y, kingdom):
        self.kingdom = kingdom
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.kingdom.is_alive():
            the_player.hp = the_player.hp - self.kingdom.damage
            print("This Kingdom has {} Army. You have {} Army remaining.".format(self.kingdom.damage, the_player.hp))

    def available_actions(self):
        if self.kingdom.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.kingdom)]
        else:
            return self.adjacent_moves()

class EstablishPeace(Westroes):
    def intro_text(self):
        return """
       Rule the conquered lands and establish the peace
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class Sunspear(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, kingdoms.Drone())
 
    def intro_text(self):
        if self.kingdom.is_alive():
            return """
            Martell Army attacks you 
            """
        else:
            return """
            You defeated their army and conquered Dorne
            """


class North(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, kingdoms.Stark())

    def intro_text(self):
        if self.kingdom.is_alive():
            return """
             Stark Army with their wolves attacks you
             """
        else:
            return """
            You defeated their army and King of the North
             """


class StormLands(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, kingdoms.Baretheon())

    def intro_text(self):
        if self.kingdom.is_alive():
            return """
            Baretheon Army attacks you 
            """
        else:
            return """
            You defeated their army and conquered Stormlands
            """


class Dragonlands(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, kingdoms.Targaryen())

    def intro_text(self):
        if self.kingdom.is_alive():
            return """
            Targareyan Army attacks you with dragons 
            """
        else:
            return """
            You defeated their Dragons and conquered your HOME LAND. Its a great victory
            """


class RichLands(TreasureArea):
    def __init__(self, x, y):
        super().__init__(x, y, army.Treasure(20))
 
    def intro_text(self):
        return """
        You conquered and stopped at Lannister Kingdom which has lots of treasure and fertile lands
        """

class LordOfWestoroes(Westroes):
    def intro_text(self):
        return """
        You are now King of the Andals, the Rhoynar, and the First Men Lord of the Seven Kingdoms
         Protector of the Realm  Prince of Dragonstone
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True