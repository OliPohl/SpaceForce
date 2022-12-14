using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WallSpawnerScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] public GameObject WallSet;

    
    private Vector2 ScreenBounds;
    private float ObjectWidth;
    private float ObjectHeight;

    private float NextSpawn = 0.0f;


    void Start()
    {
        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.       
    }


    void Update()
    {
        SpawnWalls();
    }


    private void SpawnWalls()
    {
        if (Time.time > NextSpawn)
        {
            NextSpawn = Time.time + ((10 - GameSettings.WallSpawnrate)/2);    // Resets time

            var Position = new Vector3( ScreenBounds.x + 2,   // Gets object width and screen size to mark a spawn area
                                        Random.Range(-5, 5),      // Gets object height and screen size to mark a spawn area
                                        0.0f);

            Instantiate(WallSet, Position, Quaternion.identity);   // Spawns Cube
        }
    }
}
