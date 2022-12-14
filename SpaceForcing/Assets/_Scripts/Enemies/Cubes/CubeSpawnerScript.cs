using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    ####################################################
    #               CubeSpawnerScript.cs               #
    #--------------------------------------------------#
    # This script spawns cubes to the right of the     #
    # screen.                                          #
    # Spawnrate is given in: GameSettings.cs           #
    ####################################################
*/  
public class CubeSpawnerScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] public GameObject Cube;

    
    private Vector2 ScreenBounds;
    private float ObjectWidth;
    private float ObjectHeight;

    private float NextSpawn = 0.0f;


    void Start()
    {
        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.

        ObjectWidth = Cube.transform.GetComponent<SpriteRenderer>().bounds.size.x;   // cubes width.
        ObjectHeight = Cube.transform.GetComponent<SpriteRenderer>().bounds.size.y;  // cubes height.
    }

    
    void Update()
    {
        SpawnCubes();
    }

    private void SpawnCubes()
    {
        if (Time.time > NextSpawn)
        {
            NextSpawn = Time.time + ((10 - GameSettings.CubeSpawnrate) / 7);    // Resets time

            var Position = new Vector3( Random.Range(ScreenBounds.x + (ObjectWidth * 2), ScreenBounds.x + (ObjectWidth * 4)),   // Gets object width and screen size to mark a spawn area
                                        Random.Range(ScreenBounds.y - ObjectHeight, (ScreenBounds.y - ObjectHeight) * -1),      // Gets object height and screen size to mark a spawn area
                                        0.0f);

            Instantiate(Cube, Position, Quaternion.identity);   // Spawns Cube
        }
    }
}
