using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SniperScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;

    [SerializeField] private GameObject SniperLeft;
    [SerializeField] private GameObject SniperRight;
    [SerializeField] private GameObject BeamHighlight;
    [SerializeField] private GameObject BeamAttack;


    private Vector2 ScreenBounds;
    private float SniperWidth;
    private Vector3 SniperLeftPos;
    private GameObject SniperSpawner;
    private float AnimationSpeed = 0.005f;
    private bool Intro = true;

    void Start()
    {
        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));  // Getting the screen width and height with camera units.

        SniperWidth = SniperLeft.transform.GetComponent<BoxCollider2D>().bounds.size.x;   // Gives half of the snipers width.

        SniperLeft.transform.position = new Vector3((ScreenBounds.x * -1) - (SniperWidth * 1.01f), 0, 0);   // Setting Sniper Position just outside of the screen
        SniperRight.transform.position = new Vector3(ScreenBounds.x + (SniperWidth * 1.01f), 0, 0);         // Setting Sniper Position just outside of the screen

        SniperSpawner = GameObject.FindGameObjectWithTag("SniperSpawner");  // finding SniperSpawner for outro
    }


    void Update()
    {
        SniperLeftPos = SniperLeft.transform.position;
        if (Intro){_Intro();}
        if (!SniperSpawner.activeInHierarchy){Outro();} // if SniperSpawner is not active play outro

        if (!Intro)
        {

        }

    }


    private void _Intro()   // Moves both snipers into screen
    {
        if (SniperLeftPos.x <= ((ScreenBounds.x * -1) + (SniperWidth/2)))
        {
            SniperLeft.transform.position = SniperLeftPos + new Vector3(AnimationSpeed, 0, 0);
            SniperRight.transform.position = (SniperLeftPos * -1) - new Vector3(AnimationSpeed, 0, 0);
        }
        else
        {
            Intro = false;
        }
    }


    private void Outro()   // Moves both snipers out of screen if SniperSpawner is hidden
    {
        Intro = false;
        if (SniperLeftPos.x >= (ScreenBounds.x * -1) - (SniperWidth * 1.01f))
        {
                SniperLeft.transform.position = SniperLeftPos + new Vector3(-AnimationSpeed, 0, 0);
                SniperRight.transform.position = (SniperLeftPos * -1) - new Vector3(-AnimationSpeed, 0, 0);
        }
        else
        {
            Destroy(gameObject);
        }
    }
}
