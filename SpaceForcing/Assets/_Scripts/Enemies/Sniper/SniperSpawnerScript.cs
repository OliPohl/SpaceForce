using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    ####################################################
    #              SniperSpawnerScript.cs              #
    #--------------------------------------------------#
    # This script spawns Snipers to the right of the   #
    # screen.                                          #
    # SpawnCount is given in: GameSettings.cs          #
    ####################################################
*/ 
public class SniperSpawnerScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] public GameObject SniperSet;

    private Vector2 ScreenBounds;


    void Start()
    {
        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.
        SpawnSnipers();       
    }


    void Update()
    {  
        // just does it once actived
    }


    private void SpawnSnipers()   // Spawns Snipers based on SniperCound in settings
    {
        float TempSniperCount = (float)GameSettings.SniperCount;

        for (int i = 1; i < GameSettings.SniperCount +1; i++)
        {
            float j = (float)i;
            Vector3 Pos = new Vector3(0.0f, ((ScreenBounds.y / 2f) - ((ScreenBounds.y / TempSniperCount +1f) *j)), 0.0f);
            Instantiate(SniperSet, Pos, Quaternion.identity);
        }
    }
}
