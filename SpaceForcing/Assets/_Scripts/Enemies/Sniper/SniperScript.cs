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
    private bool Outro = false;

    private float NextAim = 0.0f;
    private int Count = -1;
    private bool Aiming = true;

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
        if (Outro)
        {
            _Outro();
        }
        else if (Intro)
        {
            _Intro();
        }
        else
        {
            AimFire();
        }
    }


    private void _Intro()   // Moves both snipers into screen
    {
        SniperLeftPos = SniperLeft.transform.position;
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


    private void _Outro()   // Moves both snipers out of screen if SniperSpawner is hidden
    {
        SniperLeftPos = SniperLeft.transform.position;
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


    private void AimFire() 
    {
        if (Time.time > NextAim)    // counts every aiming cycle
        {
            NextAim = Time.time + (GameSettings.AimingTime / 7); 
            Aiming = !Aiming;
            Count += 1;
        }

        if (Count <= GameSettings.AimingCycles *2)  // if count is under  AimingCylce go aim
        {
            BeamAttack.SetActive(false);
            if (Aiming)
            {
                BeamHighlight.SetActive(true);
            }
            else
            {
                BeamHighlight.SetActive(false);
            }  
        }
        else
        {
            BeamAttack.SetActive(true);
            if (Count == (GameSettings.AimingCycles +2) *2) // Resets all values after 2 cycles of attacking
            {
                BeamHighlight.SetActive(false);
                BeamAttack.SetActive(false);
                Count = 0;

                if (!SniperSpawner.activeInHierarchy){Outro = true;} // if SniperSpawner is not active play outro
            }
        }
    }
}